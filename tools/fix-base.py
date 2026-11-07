#!/usr/bin/env python3
"""Prefix root-absolute /assets URLs for GitHub Pages project hosting."""
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/"dist"; BASE="/ultrascale-playbook_zh"
SUF={".html",".css",".js",".json"}
def main():
    n=0
    for p in DIST.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in SUF: continue
        try: s=p.read_text()
        except UnicodeDecodeError: continue
        t=s.replace('"/assets/','"'+BASE+'/assets/').replace("'/assets/","'"+BASE+"/assets/")
        t=t.replace('(/assets/','('+BASE+'/assets/')
        for q in ('"',"'",'`'):
            t=t.replace(q+'../assets/',q+BASE+'/assets/')
        if t!=s: p.write_text(t); n+=1
    print("rewrote",n,"files")
if __name__=="__main__": main()
