import DS from 'ember-data';
import { computed } from '@ember/object'
import moment from 'moment';
const { Model } = DS;

export default Model.extend({
    title: DS.attr(),
    presenter: DS.attr(),
    time: DS.attr(),
    location: DS.attr(),
    description: DS.attr(),
    formattedTime: computed('time', function() {
        return moment(this.time).format("ddd @ h:mm a, MMMM D, YYYY")
    })
});
