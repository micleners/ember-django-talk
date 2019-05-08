import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
    store: service(),

    model() {
        const events = this.get('store').findAll('event');
        return events;
    }
});
