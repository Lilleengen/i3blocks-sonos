#!/usr/bin/env python3
#
# By Henrik Lilleengen (mail@ithenrik.com)
#
# Released under the MIT License: https://opensource.org/licenses/MIT

import soco, sys

speakers = list(soco.discover())

if len(speakers) > 0:
    state = speakers[0].get_current_transport_info()['current_transport_state']

    if state == 'PLAYING':
        if len(sys.argv) > 1 and sys.argv[1] == "1":
            speakers[0].stop()
            print("")
        else:
            track = speakers[0].get_current_track_info()
            print(" " + track['title'] + " - " + track['artist'])
    else:
        if len(sys.argv) > 1 and sys.argv[1] == "1":
            speakers[0].play()
            track = speakers[0].get_current_track_info()
            print(" " + track['title'] + " - " + track['artist'])
        else:
            print("")
