import Controller from "@ember/controller";
import { computed } from '@ember/object';
import moment from 'moment';

export default Controller.extend({
  form: computed(function() {
    return {
      title: "",
      presenter: "",
      time: "",
      location: "",
      description: "",
    }
  }),

  actions: {
    saveEvent() {
      const now = moment().format('YYYY-MM-DDThh:mm:ssZ')
      const time = this.form.time ? `${this.form.time}-05:00` : now
      const newEvent= this.store.createRecord("event", {
        title: this.form.title,
        presenter: this.form.presenter,
        time: time,
        location: this.form.location,
        description: this.form.description
      });
      newEvent.save().then((event) => {
        this.notifyPropertyChange('form');
        this.transitionToRoute('event', event);
      })
    }
  }
});
