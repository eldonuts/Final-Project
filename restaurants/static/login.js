// FACEBOOK LOGIN API

window.fbAsyncInit = function() {
FB.init({
  appId      : '1158039014215879',
  xfbml      : true,
  version    : 'v2.5'
});
};

(function(d, s, id){
 var js, fjs = d.getElementsByTagName(s)[0];
 if (d.getElementById(id)) {return;}
 js = d.createElement(s); js.id = id;
 js.src = "//connect.facebook.net/en_US/sdk.js";
 fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));


function fb_login(state){
    FB.login(function(response) {

        if (response.authResponse) {
            $('#facebookloading').attr('style', 'display: inline');
            $('#facebooklogo').attr('style', 'display: none');

            console.log('Welcome!  Fetching your information.... ');
            access_token = response.authResponse.accessToken; //get access token
            user_id = response.authResponse.userID; //get FB UID

            FB.api('/me', function(response) {
                user_email = response.email; //get user email
                 $.ajax({
                  type: 'POST',
                  url: ('/login_facebook?state=' + state),
                  processData: false,
                  data: access_token,
                  contentType: 'application/octet-stream; charset=utf-8',
                  success: function(result) {
                    // Handle or verify the server response if necessary.
                    if (result) {
                        window.location.href = "/";
                  } else {
                        console.log('Failed to log in');
                     }
                  }

                });
            });

        } else {
            //User hit cancel button
            console.log('User cancelled login or did not fully authorize.');

        }
    }, {
        scope: 'public_profile,email'
    });
}


// GOOGLE LOGIN API

function start() {
      gapi.load('auth2', function() {
        auth2 = gapi.auth2.init({
          client_id: '298600907503-fgm7p78ilnj0rvktun02om0r5lqiel00.apps.googleusercontent.com'
        });
      });
    }