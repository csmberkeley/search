import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Links } from '../../../api/links.js';
 
import './layout.html';
import './layout.css';
import './layout.routes.js';
import '../link/link.js';

Template.layout.onCreated(function () {
  this.input = new ReactiveVar('');
  this.searchBox = $('.search-box');
  Meteor.subscribe('links');
});

Template.layout.onCreated(function () {
  this.practice = new ReactiveVar(true);
  this.labs = new ReactiveVar(true);
  this.notes = new ReactiveVar(true);
  this.slides = new ReactiveVar(true);
  // this.searchBox = $('.search-box');
  // Meteor.subscribe('links');
});

Template.layout.onRendered(function () {
  this.searchBox = $('.search-box');
  this.searchBox.addClass('search-none');
})
 
Template.layout.helpers({
  links() {
    const instance = Template.instance();
    const currInput = instance.input.get();
    if (currInput !== undefined && currInput !== null && currInput.length > 0) {
      var arr =  [];
      if(instance.practice.get() == true) {
        arr.push("Problem");
      }
      if (instance.labs.get() == true) {
        arr.push("Lab")
      }
      let results = Links.find({title: {$regex: '.*' + currInput.toLowerCase() + '.*'}});

      if (results.count() === 0) {
        instance.searchBox.addClass('search-none');
      } else {
        instance.searchBox.removeClass('search-none');
        return results;
      }
    } else {
      if (instance.searchBox) {
        instance.searchBox.addClass('search-none');
      }
    }
  },
});

Template.layout.events({
  'input .search-field'(event, instance) {
    event.preventDefault();
    instance.input.set(event.target.value);
  },
});

Template.layout.events({
'change input'(event, instance) {

  var x = event.target.value;
  if (x == 'practice') {
    instance.practice.set(event.target.checked);
  }
  else if (x == 'labs')
  {
    instance.labs.set(event.target.checked);
  }
  // Session.set("statevalue", x);
  // console.log(x);
  // TODO: ADD MORE HERE!!

 }
});
