import Controller from '@ember/controller';
import { computed } from '@ember/object';
import { inject as service } from '@ember/service';

export default Controller.extend({
    store: service(),
    showCreateForm: false,
    showEditForm: false,
    newEvent: computed(function() {
      return this.store.createRecord('event');
    }),
    
    actions: {
        toggleCreateForm() {
          this.toggleProperty('showCreateForm');
        },
        
        toggleEditForm() {
          this.toggleProperty('showEditForm');
        },
        
        createSave() {
          this.notifyPropertyChange('newEvent');
          this.set('showCreateForm', false);
        },

        createCancel() {
          this.set('showCreateForm', false);
        },

        editSave() {
          this.notifyPropertyChange('newEvent');
          this.set('showEditForm', false);
        },

        editCancel() {
          this.set('showEditForm', false);
        },

        delete(event) {
          event.destroyRecord()
        },
    }
});
