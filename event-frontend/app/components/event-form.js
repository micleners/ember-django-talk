import Component from '@ember/component';
import { computed } from '@ember/object';
import moment from 'moment';
import { inject as service } from '@ember/service';

export default Component.extend({
  store: service(),
  form: computed(function() {
    const time = this.event.time ? moment(this.event.time).format('YYYY-MM-DDTHH:mm:ss') : ''
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
            'time': time,
            'location': this.form.location,
            'description': this.form.description,
        });
        this.event.save().then(() => {
            this.save();
            this.notifyPropertyChange('form');
        })
    },
    eventCancel() {
        this.cancel();
    }
  }
});
