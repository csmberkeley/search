import { Mongo } from 'meteor/mongo';
 
export const Links = new Mongo.Collection('links');
export const LinkProps = {
  types: ['practice', 'notes', 'slides', 'lab']
}

Meteor.methods({

});
