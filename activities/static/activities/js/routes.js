App.Router.map(function(){
   this.resource('activities', {path: '/'});

});

App.ActivitiesRoute = Ember.Route.extend({
    model: function(){
        console.log("Getting model");
        return this.store.findAll('activity');
    }
});