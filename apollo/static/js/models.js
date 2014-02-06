App.Activity = DS.Model.extend({
    url: "activities",
	name: DS.attr("string"),
	//category: DS.hasMany("App.Category"),
	description: DS.attr("string"),
});

//App.Category = DS.Model.extend({
//    name: DS.attr("string")
//});

App.User = DS.Model.extend({
    url:"users",
    username: DS.attr("string")
});