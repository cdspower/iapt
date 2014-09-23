# -*- coding: utf-8 -*-
# @IAPT: Very simple controller

def index():
    # @IAPT: nested dictionary to provide us with some data
    features = dict(
        book1={'id': '1', 'name': 'Batman: Arkham Asylum', 'price': '9.00', 'type': 'Book', 'writer': 'Grant Morrison',
               'pages': '216',
               'description': 'Written by Grant Morrison. Art and cover by Dave McKean In celebration of the 16th anniversary of the critically acclaimed Batman story that helped launch the U.S. careers of Grant Morrison and Dave McKean, DC Comics is proud to present a softcover edition of the Arkham Asylum Anniversary Edition, reprinting the now-classic confrontation between the Dark Knight and his archnemeses the Joker, Two-Face, Scarecrow, Poison Ivy, and more in the black heart of Gotham City\'s house for the criminally insane.',
               'publisher': 'DC Comics'},
        book2={'id': '2', 'name': 'Superman: Earth One', 'pages': '176', 'writer': 'J. Michael  Straczynski',
               'price': '7.00',
               'type': 'Book',
               'description': 'J. Michael Straczynski, the creator of Babylon 5, joins forces with rising star artist Shane Davis (Superman/Batman: The Search for Kryptonite) to create this original graphic novel that gives new insight into Clark Kent\'s transformation into Superman and his first year as The Man of Steel. This is the first in a new wave of original DC Universe graphic novels, featuring top writers and illustrators unique takes on DC characters.',
               'publisher': 'DC Comics'},
        book3={'id': '3', 'name': 'Wonder Woman: Eyes of the Gorgon', 'writer': 'Greg Rucka', 'pages': '144',
               'price': '8.00', 'type': 'Book',
               'description': 'Written by Greg Rucka Art by Drew Johnson, James Raiz, Sean Phillips and Ray Snyder. Cover by J.G. Jones. A new volume collecting WONDER WOMAN &#35;206-213! The deadly Medousa comes calling, and Wonder Womans world is turned completely upside-down. After a terrible sacrifice, the Amazing Amazon must prove herself once again to her comrades in the JLA and to the world!',
               'publisher': 'DC Comics'})
    return dict(features=features)
