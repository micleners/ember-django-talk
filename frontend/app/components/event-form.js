import Component from '@ember/component';
import { computed } from '@ember/object';
import moment from 'moment';

export default Component.extend({
  form: computed(function() {
    const time = moment(this.event.time).format('YYYY-MM-DDTHH:mm:ss')
      console.log(time)
    return {
      title: this.event.title,
      presenter: this.event.presenter,
      time: time,
      location: this.event.location,
      description: this.event.description,
    }
  }),

  actions: {
    eventSave() {
        const now = moment().format('YYYY-MM-DDThh:mm:ssZ')
        const time = this.form.time ? `${this.form.time}-05:00` : now
        this.event.setProperties({
            'title': this.form.title,
            'presenter': this.form.presenter,
            'time': this.form.time,
            'location': this.form.location,
            'description': this.form.description,
        });
        console.log(this.event)
        this.event.save().then((event) => {
            this.notifyPropertyChange('form');
            this.transitionToRoute('event', event);
        })
        this.changeSave();
    },
    eventCancel() {
        this.changeCancel();
    }
  }
});
