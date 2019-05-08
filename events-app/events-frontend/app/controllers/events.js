import Controller from '@ember/controller';

export default Controller.extend({
  actions: {
    delete(event) {
      event.destroyRecord()
    },
  }
});
