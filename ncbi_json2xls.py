# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 14:25:45 2022

@author: Administrator
"""
import sys
import re
import json
json_file=sys.argv[1].strip()
output=sys.argv[2].strip()
#json_file='Arabidopsis.txt'
#output='Eukaryota.2023-08-11.xls'
with open(json_file, 'r') as f:
    data = json.load(f)
sp_list=data['reports']


f=open(output,'w')
f.write('sci_name\tass_level\tass_id\tchr_num\tcontig_N50\tseq_len\tprotein_coding_gene_num\tgenome_path\tgff_path\tbusco_lineage\tsequencing_tech\tsubmission_date\n')
for i in range(len(sp_list)):
    a=sp_list[i]
    ass_id=a['accession']
    sci_name=a['organism']['organism_name']
    ass_level=a['assembly_info']['assembly_level']
    N50=str(a['assembly_stats']['contig_n50'])
    seq_len=str(a['assembly_stats']['total_sequence_length'])
    sub_date=a['assembly_info']['release_date']
    display=a['assembly_info']['assembly_name']
    try:
        gene_num=str(a['annotation_info']['stats']['gene_counts']['protein_coding'])
    except:
        gene_num='NA'
    tmp=re.split("",ass_id)[1:-1]
    genome_path="https://ftp.ncbi.nlm.nih.gov/genomes/all/"+''.join(tmp[:3])+"/"+''.join(tmp[4:7])+"/"+''.join(tmp[7:10])+"/"+''.join(tmp[10:13])+'/'+ass_id+'_'+display+'/'+ass_id+'_'+display+"_genomic.fna.gz"
    try:
        gff_path="https://ftp.ncbi.nlm.nih.gov/genomes/all/"+''.join(tmp[:3])+"/"+''.join(tmp[4:7])+"/"+''.join(tmp[7:10])+"/"+''.join(tmp[10:13])+'/'+ass_id+'_'+display+'/'+ass_id+'_'+display+"_genomic.gff.gz"
    except:
        gff_path="NA"
    if gene_num=='NA':
        gff_path="NA"
    try:
        busco_lineage=a['annotation_info']['busco']['busco_lineage']
    except:
        busco_lineage="NA"
    try:
        sequencing_tech=a['assembly_info']['sequencing_tech']
    except:
        sequencing_tech="NA"
    try:
        chr_num=str(a['assembly_stats']['total_number_of_chromosomes'])
    except:
        chr_num="NA"
    f.write(sci_name+'\t'+ass_level+'\t'+ass_id+'\t'+chr_num+'\t'+N50+'\t'+seq_len+'\t'+gene_num+'\t'+genome_path+'\t'+gff_path+'\t'+busco_lineage+'\t'+sequencing_tech+'\t'+sub_date+'\n')
f.close()
