#!/usr/bin/awk -f

NR > 2 && $1 != "postgres" {
	print $3
}
