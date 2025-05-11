#!/usr/bin/env python3

import openreview
import sys
import bibtexparser
import os
from dotenv import load_dotenv

load_dotenv()


def get_v1_rejections(client, paper_title):
    rejections = []
    notes = client.search_notes(term=paper_title, content='all', source='all', group='all', limit=5)
    for note in notes:
        if 'title' in note.content and note.content['title'] == paper_title:
            for subnote in client.get_notes(forum=note.forum):
                if 'decision' in subnote.content:
                    decision = subnote.content['decision'].lower()
                    if 'reject' in decision:
                        rejections.append(note.forum)
    return rejections


def get_v2_rejections(client, paper_title):
    rejections = []
    notes = client.search_notes(term=paper_title, content='all', source='all', group='all', limit=5)
    for note in notes:
        if 'title' in note.content and note.content['title']['value'] == paper_title:
            for subnote in client.get_notes(forum=note.forum):
                if 'decision' in subnote.content:
                    decision = subnote.content['decision']['value'].lower()
                    if 'reject' in decision:
                        rejections.append(note.forum)
    return rejections


if __name__ == "__main__":
    # Ensure a filepath is passed
    if len(sys.argv) < 2:
        print("Usage: python main.py path/to/file.bib")
        sys.exit(1)

    # Load the .bib file
    bib_path = sys.argv[1]
    with open(bib_path, 'r', encoding='utf-8') as bibfile:
        bib_database = bibtexparser.load(bibfile)

    client_v1 = openreview.Client(
        baseurl='https://api.openreview.net',
        username=os.getenv('OPENREVIEW_USERNAME'),
        password=os.getenv('OPENREVIEW_PASSWORD')
    )

    client_v2 = openreview.api.OpenReviewClient(
        baseurl='https://api2.openreview.net',
        username=os.getenv('OPENREVIEW_USERNAME'),
        password=os.getenv('OPENREVIEW_PASSWORD')
    )

    total_entries = len(bib_database.entries)
    for index, bib_entry in enumerate(bib_database.entries):
        paper_title = bib_entry.get('title', '').replace('{', '').replace('}', '')

        if not paper_title:
            print("No title found in .bib file for entry:")
            continue

        rejections = get_v1_rejections(client_v1, paper_title) + get_v2_rejections(client_v2, paper_title)

        if len(rejections) > 0:
            print(f"⛔️ [REJECTED] ({index + 1}/{total_entries}) {paper_title}")
            for forum_id in rejections:
                print(f"    > https://openreview.net/forum?id={forum_id}")
        else:
            print(f"✅ [OK] ({index + 1}/{total_entries}) {paper_title}")
