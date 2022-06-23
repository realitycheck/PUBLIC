package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
	"net/http/httputil"
)

func main() {
	http.Handle("/", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		dump, err := httputil.DumpRequest(r, true)
		if err != nil {
			http.Error(w, fmt.Sprint(dump), http.StatusInternalServerError)
			return
		}
		fmt.Fprintf(w, "%q", dump)
		log.Printf("%s", dump)
	}))

	port := flag.String("p", "2019", "port")
	flag.Parse()

	http.ListenAndServe("0.0.0.0:"+*port, nil)
}
