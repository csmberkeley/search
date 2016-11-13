# search61b
Inspired by the instant search on [cs61a.org](cs61a.org). I also wanted to try using React on top of Meteor.

Meteor stuff in in `app/`, a MongoDB populator and some scrapers in `utils/`

## Setup
1. Get [Meteor](https://www.meteor.com/install)
2. Run `meteor npm install`
3. Run `meteor`. You can keep this running as you make changes; Meteor automatically refreshes the web server.

## File Structure
- `imports/api` - Model layer for object CRUD
- `imports/ui/components` - directories divided by component name
  - `layout` defines overall layout and wraps individual templates
    - Global events or helpers should go in `layout.js`
  - Controller logic + Blaze template should only go in its directory
  - Component-specific CSS should go in corresponding folder and be imported by corresponding `.js` file
- `imports/ui/components/layouts/layout.routes.js` - Routes are here
- `server` - imports
- [More notes from Meteor docs](https://guide.meteor.com/structure.html)

## Misc.
- [The Blaze docs are here now](http://blazejs.org/guide/introduction.html)
- We are using [Flat UI](http://designmodo.github.io/Flat-UI/) for our front-end (docs are [here](https://designmodo.github.io/Flat-UI/docs/components.html))




