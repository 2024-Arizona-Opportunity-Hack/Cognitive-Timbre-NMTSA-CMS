function onApiLoad() {
    gapi.load('auth', {'callback': onAuthApiLoad});
    gapi.load('picker', {'callback': onPickerApiLoad});
}

function onAuthApiLoad() {
    window.gapi.auth.authorize(
        {
            'client_id': GOOGLE_CLIENT_ID,
            'scope': ['https://www.googleapis.com/auth/drive.file'],
            'immediate': false
        },
        handleAuthResult
    );
}

function onPickerApiLoad() {
    // Picker API loaded
}

function handleAuthResult(authResult) {
    if (authResult && !authResult.error) {
        createPicker();
    } else {
        console.log('Error: ' + authResult.error);
    }
}

function createPicker() {
    var picker = new google.picker.PickerBuilder()
        .addView(google.picker.ViewId.DOCS)
        .setOAuthToken(gapi.auth.getToken().access_token)
        .setDeveloperKey(DEVELOPER_KEY)
        .setCallback(pickerCallback)
        .build();
    picker.setVisible(true);
}

function pickerCallback(data) {
    if (data.action == google.picker.Action.PICKED) {
        var fileId = data.docs[0].id;
        var fileUrl = data.docs[0].url;
        // Handle the selected file URL
        console.log('Selected file URL: ' + fileUrl);
    }
}