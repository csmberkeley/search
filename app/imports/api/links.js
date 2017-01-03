/*
Everything is a string

Required fields {
  _id:              (Primary Key) URL of the link
  formatted_title:  Readable link title
  type:             What kind of material is linked
  semester:         The semester the material is from
}
Optional fields {
  title:            Searchable form of the link's title
  topics:           What general CS 61B the link fits into
}
*/

import { Mongo } from 'meteor/mongo';
 
export const Links = new Mongo.Collection('links');
export const LinkProps = {
  types: ['practice', 'notes', 'slides', 'lab']
}

Meteor.methods({

});
