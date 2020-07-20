#!/usr/bin/perl -w
use strict;
############################################################
#This script is to convert multiple tab-delimited files to #
#Excel sheets. xie186@purdue.edu                           #
############################################################
use Excel::Writer::XLSX;

my ($tab, $sheetname, $out) = @ARGV;
die usage() unless @ARGV == 3;
sub usage{
    my $die =<<DIE;
perl *.pl <Input file: tab-delemited file [file1,file2...]> <SheetName[Sheet1,Sheet2...]> <output file in XLSX file>
DIE
}
my $workbook = Excel::Writer::XLSX->new($out);

my @tab = split(/,/, $tab);

my @sheetname = split(/,/, $sheetname);
#my worksheet=workbook->add_worksheet();
for(my $i = 0; $i < @tab; ++$i){
    my $row = 0;
    my $worksheet = $workbook->add_worksheet($sheetname[$i]);
    open TAB, $tab[$i] or die "$!";
    while(<TAB>){
        chomp;
        my @ele = split(/\t/);
        &write_xlsx($worksheet, $row, @ele);
        ++$row;
    }
}

sub write_xlsx{
    my ($worksheet, $tem_row, @ele) = @_;
    for(my $i = 0; $i < @ele; ++$i){
        $worksheet->write( $tem_row, $i, $ele[$i]);
    }
}
