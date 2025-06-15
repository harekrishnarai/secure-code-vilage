package main

import "log"

func logCredentials(user, pass string) {
    log.Printf("%s:%s", user, pass)
}
