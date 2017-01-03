import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Links, LinkProps } from '../../../api/links.js';
 
import './layout.html';
import './layout.css';
import '../link/link.js';

Template.layout.onCreated(function () {
  this.input = new ReactiveVar('');
  this.typeFilter = new ReactiveDict();

  const self = this;
  _.each(LinkProps.types, function(type) {
    self.typeFilter.set(type, true);
  });

  Meteor.subscribe('links');
});

Template.layout.onRendered(function () {
  this.searchBox = $('.search-box');
  this.searchBox.addClass('search-none');
  $(':checkbox').radiocheck();
});

/*
  TODO: Topics have been added into database. Order results by weight system
  
  Title match: more weight
  Reverse topic match: less weight
*/
function constructMongoQuery(currInput, instance) {
  const query = {};
  const types = [];
  _.each(LinkProps.types, function(type) {
    if (instance.typeFilter.get(type)) {
      types.push(type);
    }
  });

  query.title = { $regex: currInput.toLowerCase() };
  if (types.length < 4) {
    query.type = { $in: types };
  }

  return query;
}
 
Template.layout.helpers({
  links() {
    const instance = Template.instance();
    const currInput = instance.input.get();

    if (currInput) {
      let results = Links.find(constructMongoQuery(currInput, instance));

      if (results.count() !== 0) {
        return results;
      }
    }
  },
});

Template.layout.events({
  'input .search-field'(event, instance) {
    event.preventDefault();
    instance.input.set(event.target.value);
  },
  'change .type-filters input'(event, instance) {
    event.preventDefault();
    instance.typeFilter.set(event.target.id, event.target.checked);
  },
});
