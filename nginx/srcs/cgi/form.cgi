#!/usr/bin/perl

# HTML HEADER
print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD>\n";
print "<META HTTP-EQuiv=\"Content-Type\" Content=\"text/html; charset=Shift_JIS\">";
print "<TITLE>CGI Sample (Answer)</TITLE>\n";
print "</HEAD>\n";
print "\n";

print "<BODY BGCOLOR=#FFFFFF TEXT=#000000>\n";

print "\n";
print "<CENTER>\n";
print "<FONT SIZE=+2>\n";
print "<I><B><FONT COLOR=#007744>CGI Sample (Answer)</FONT></I></B>\n";
print "</FONT><BR>\n";
print "<BR>\n";

read(STDIN,$buffer,$ENV{'CONTENT_LENGTH'});
@pairs=split(/&/,$buffer);
foreach $pair(@pairs) {
    ($name,$value)=split(/=/,$pair);
    $value=~tr/+/ /;
    $value=~s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/eg;

    printf ("NAME: %s,  VALUE: %s<BR>\n", $name, $value);
}

print "\n";
print "</BODY>\n";

print "</HTML>\n";