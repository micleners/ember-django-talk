import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
    store: service(),

    model(event) {
        return this.store.findRecord('event', event.event_id);
    }
});
