from dogs import db, Dogs
# setup the 20 name list. Run only once or duplicates will form
db.create_all()

Brady = Dogs('Nikola', 'Dale', 'Brady', '2')
Buddy = Dogs('Harri', 'Camacho', 'Buddy', '5')
Hazel = Dogs('Yousaf', 'Hewitt', 'Hazel', '1')
Minnie = Dogs('Howard', 'Person', 'Minnie', '7')
Cody = Dogs('Felicity', 'Turnbull', 'Cody', '6')
Lucky = Dogs('Akbar', 'Bridges', 'Lucky', '5')
Gizmo = Dogs('Warwick', 'Castillo', 'Gizmo', '3')
Princess = Dogs('Timur', 'Metcalfe', 'Princess', '2')
Gunner = Dogs('Tess', 'Reilly', 'Gunner', '1')
Katie = Dogs('Monty', 'Mercado', 'Katie', '10')
Layla = Dogs('Crystal', 'Francis', 'Layla', '8')
Foxy = Dogs('Reece', 'Stamp', 'Foxy', '6')
Winnie = Dogs('Kieron', 'Banks', 'Winnie', '4')
Ranger = Dogs('Shanai', 'Davidson', 'Ranger', '3')
Bandit = Dogs('Tyreke', 'Martin', 'Bandit', '1')
Emma = Dogs('Reegan', 'Timms', 'Emma', '2')
Sugar = Dogs('Darcie', 'Frame', 'Sugar', '2')
Grace = Dogs('Hanna', 'Shelton', 'Grace', '3')
Murphy = Dogs('Duncan', 'Sanders', 'Murphy', '3')
Lily = Dogs('Kaydee', 'Mclaughlin', 'Lily', '6')

db.session.add_all([Brady, Buddy, Hazel, Minnie, Cody, Lucky, Gizmo, Princess, Gunner, Katie, Layla, Foxy, Winnie,
                    Ranger, Bandit, Emma, Sugar, Grace, Murphy, Lily])
db.session.commit()

print(Brady.id)
