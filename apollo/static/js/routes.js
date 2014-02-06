App.Router.map(function(){
   this.resource('activities', {path: '/'});

});

App.ActivitiesRoute = Ember.Route.extend({
    model: function(){
        return this.store.findAll('activity');
    }
});