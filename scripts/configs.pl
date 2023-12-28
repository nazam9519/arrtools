#!/usr/bin/perl
use Config::Simple;
use strict;
use warnings;

my ($conf) = @ARGV;
if(not defined $conf){
    die "Please supply an the path to the config file";
}elsif(! -e $conf){
    die "Could not find file name $conf";
}
my $cfg = new Config::Simple($conf);
my $home = $cfg->param("tarrhome");
$home = "$home/docker/data";
print "homedir is: $home\n";

