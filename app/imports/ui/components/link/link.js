import { Template } from 'meteor/templating';
import { Links } from '../../../api/links.js';
import './link.html';

Template.link.events({
  'mouseenter .link'(event) {
    $(event.target).addClass('todo-done');
  },
  'mouseleave .link'(event) {
    $(event.target).removeClass('todo-done');
  },
  'click .link'(event) {
    window.open(this.url, '_blank');
  }
});
