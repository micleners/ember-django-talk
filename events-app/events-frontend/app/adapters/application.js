import DS from 'ember-data';
import { computed } from '@ember/object';

export default DS.JSONAPIAdapter.extend({
  host: computed(function(){
    return 'http://localhost:8000';
  }),
  namespace: 'api',
  buildURL: function(type, id, record) {
  //call the default buildURL and then append a slash
  return this._super(type, id, record) + '/';
  }
});
