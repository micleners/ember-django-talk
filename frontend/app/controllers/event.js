import Controller from "@ember/controller";
import { computed } from '@ember/object';

export default Controller.extend({
  editing: computed(() => false),

  actions: {
    delete() {
      const event = this.model;
      event.destroyRecord().then(() => {
        this.transitionToRoute('events');
      })
    },
    edit() {
      this.set('editing', true);
    },
    save() {
      this.set('editing', false);
    },
    cancel() {
      this.set('editing', false);
    }
  }
});
