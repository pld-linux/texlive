#!/bin/sh
/usr/lib/rpm/perl.req "$@" | grep -v 'perl(\(Win32\|only\|path_tre\|just\|Htex\|Pts\)'
