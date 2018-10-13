#!/usr/bin/env php

<?php
#include_once __DIR__ . '/../vendor/autoload.php';
include_once __DIR__ . '/vendor/autoload.php';
include_once "templates/base.php";

/**
 * Returns an authorized API client.
 * @return Google_Client the authorized client object
 */
function getClient()
{
    $client = new Google_Client();
    $client->setApplicationName('Google Calendar API PHP Quickstart');
    $client->setScopes(Google_Service_Calendar::CALENDAR);
    //$client->setScopes(Google_Service_Calendar::CALENDAR_READONLY);
    $client->setAuthConfig('/apps/common/UES/scs/absence/bin/client_secret.json');
    $client->setAccessType('offline');

// --------------------------------------------------------------------------
// https://developers.google.com/resources/api-libraries/documentation/calendar/v3/php/latest/class-Google_Service_Calendar_Event.html#_getId
// google-api-php-client.git => vendor/google/apiclient-services/src/Google/Service/Calendar/Calendar.php
// --------------------------------------------------------------------------
// https://console.developers.google.com/apis/credentials?project=noted-tide-202312
// Name	Creation date	Type	Client ID	 
// scs web	May 1, 2018	Web application	891605835887-7embrqk2r6u4tmkjgsa65kt6u1fb5ovr.apps.googleusercontent.com	  
// Google Calendar API scs	Apr 26, 2018	Other	891605835887-o08dnj0dv8a200j28gludjsbfo15a3kt.apps.googleusercontent.com	  
// USE ONLY "Google Calendar API scs" (type=Other=OK), not "scs" (type=web=not OK)
// --------------------------------------------------------------------------

    // Load previously authorized credentials from a file.
    //printf("L14 \n");
    // $credentialsPath = expandHomeDirectory('credentials.json');
    $credentialsPath = ('/apps/common/UES/scs/absence/bin/credentials.json');
    if (file_exists($credentialsPath)) {
        $accessToken = json_decode(file_get_contents($credentialsPath), true);
    } else {
        // Request authorization from the user.
        $authUrl = $client->createAuthUrl();
        printf("Open the following link in your browser:\n%s\n", $authUrl);
        //exit(0);
        //print 'Enter verification code: ';
// https://www.googleapis.com/auth/calendar
// <!--         
        $authCode = trim(fgets(STDIN)); 
        //$authCode = '4/AACBjP6BMD1chJ2F9-Hyg-SmtD_6IF-Tgqmly5twKZp_mBjm1MJNqEKwzooBEzEUQOjfzT5nSUP5F7dmr0tUFUw';
        //$authCode = '4/AACIS_Dj4QrWU_ezIgDdKCvsJO8IVfICb92WeFRwIDhlrkHVldcF2fTGH62R2h_Qi1MdUZcilW9NmCqCX41tAYc';
        // Exchange authorization code for an access token.
        $accessToken = $client->fetchAccessTokenWithAuthCode($authCode);


        // Store the credentials to disk.
        if (!file_exists(dirname($credentialsPath))) {
            mkdir(dirname($credentialsPath), 0700, true);
        }
        file_put_contents($credentialsPath, json_encode($accessToken));
        printf("Credentials saved to %s\n", $credentialsPath);
    }
    $client->setAccessToken($accessToken);

    // Refresh the token if it is expired.
    if ($client->isAccessTokenExpired()) {
        $client->fetchAccessTokenWithRefreshToken($client->getRefreshToken());
        file_put_contents($credentialsPath, json_encode($client->getAccessToken()));
    }
    return $client;
}

/**
 * Expands the home directory alias '~' to the full path.
 * @param string $path the path to expand.
 * @return string the expanded path.
 */
function expandHomeDirectory($path)
{
    $homeDirectory = getenv('HOME');
    if (empty($homeDirectory)) {
        $homeDirectory = getenv('HOMEDRIVE') . getenv('HOMEPATH');
    }
    return str_replace('~', realpath($homeDirectory), $path);
}


function usage($action)
{
    printf("Unknow action %s\n", $action);
    printf("Usage: php -f ./scs.php a=list|add|del\n");
    printf("  Example  a=add b='JG WFH 2018-05-05 9am (9am mandatory)'\n");
    printf("  Example a=list b=\n");
    printf("  Example  a=del b=7qircfrd9mouctbk18glvpsd8v\n");
    printf("exiting...\n");
    exit(0);
}






//  #    #    ##       #    #    #
//  ##  ##   #  #      #    ##   #
//  # ## #  #    #     #    # #  #
//  #    #  ######     #    #  # #
//  #    #  #    #     #    #   ##
//  #    #  #    #     #    #    #
// -------------------------------------------------------------------
parse_str(implode('&', array_slice($argv, 1)), $_GET);
$action = $_GET['a'];
//printf("x=%s\n", $action);

// -------------------------------------------------------------------
// Get the API client and construct the service object:
$client = getClient();
$service = new Google_Service_Calendar($client);
date_default_timezone_set('Europe/Zurich');

if(trim($action) == 'add'){
    $absence = $_GET['b'];
    printf("Adding new absence to the calendar (action=%s): ", $action);
    add_events($service, $absence);

} else if (trim($action) == 'list') {
    printf("Listing absence(s) from the calendar (action=%s)\n", $action);
    list_events($service);

} else if (trim($action) == 'del') {
    $absence = $_GET['b'];
    printf("Deleting absence from the calendar (action=%s)\n", $action);
    del_events($service, $absence);

} else {
    usage($action);
}
exit(0);

// -------------------------------------------------------------------
function list_events($service)
{
// get the list of absence ids from the calendar:
$events = $service->events->listEvents('primary');

while(true) {
  foreach ($events->getItems() as $event) {
    //printf("L100 \n");
    //echo $event->getSummary();
    printf("id=%s ",$event->getId());
    printf("start=%s ", $event->getStart()->getDateTime());
    printf("end=%s ", $event->getEnd()->getDateTime());
    printf("absence=%s \n",$event->getSummary());

//python:
//for event in events:
//    start = event['start'].get('dateTime', event['start'].get('date'))
//    print(start, event['summary'])

    //printf("L102 \n");
  }

  $pageToken = $events->getNextPageToken();

  if ($pageToken) {
    $optParams = array('pageToken' => $pageToken);
    $events = $service->events->listEvents('primary', $optParams);
  } else {
    break;
  }

}

//$event = $service->events->get('primary', .............);
//echo $event->getSummary();
exit(0);
}



// -------------------------------------------------------------------
function add_events($service, $absence)
{
// Add an absence to the calendar:
$createdEvent = $service->events->quickAdd('primary', $absence);
#    'JG WFH on 2018-05-05 10am-04pm');
//echo $createdEvent->getId();
printf("new event id=%s \n", $createdEvent->getId());
}

function del_events($service, $absence)
{
// -------------------------------------------------------------------------
// Delete an absence from the calendar:
//printf("event id=%s \n", $service->events->getId());
$service->events->delete('primary', $absence);
}

// -------------------------------------------------------------------------
// Print the next 10 events on the user calendar.
$calendarId = 'primary';
$optParams = array(
  'maxResults' => 10,
  'orderBy' => 'startTime',
  'singleEvents' => true,
  'timeMin' => date('c'),
);
$results = $service->events->listEvents($calendarId, $optParams);

if (empty($results->getItems())) {
    print "No upcoming scs absence found.\n";

} else {
    print "Upcoming absence:\n";
    foreach ($results->getItems() as $event) {
        $start = $event->start->dateTime;
        if (empty($start)) {
            $start = $event->start->date;
        }
        printf("%s (%s)\n", $event->getSummary(), $start);
    }

}

?>

<!-- echo pageHeader("jg test"); -->
<!-- <?= pageFooter(__FILE__) ?> -->
