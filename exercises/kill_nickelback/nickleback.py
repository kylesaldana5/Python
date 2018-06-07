songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Phish', 'YEM'),
    ('UmphreysMcGee', 'Ocean Billy'),
    ('Spafford', 'My Road'),
    ('Nickelback', 'Animals')
}

noNickleBack = [ song for song in songs if song[0] != 'Nickelback']
print(noNickleBack)