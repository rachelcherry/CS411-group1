def get_singer_by_state(state):
    singers_by_state = {
        'Alabama': '37i9dQZF1DZ06evO1TxlPa', #Lionel Richie
        'Alabama'.casefold(): '37i9dQZF1DZ06evO1TxlPa',
        'Alaska'.casefold: '37i9dQZF1DZ06evO3W8ISY', #Jewel
        'Alaska': '37i9dQZF1DZ06evO3W8ISY',
        'Arizona': '37i9dQZF1DZ06evO0OfBwg', #Linda Ronstadt
        'Arizona'.casefold(): '37i9dQZF1DZ06evO0OfBwg',
        'Arkansas': '37i9dQZF1DZ06evO3JKqeQ', #Johnny Cash
        'California': '37i9dQZF1DX2oU49YwtXI2', #Beyoncé
        'California'.casefold(): '37i9dQZF1DX2oU49YwtXI2',
        'Colorado': '37i9dQZF1DZ06evO4xb6jm', #John Denver
        'Colorado'.casefold(): '37i9dQZF1DZ06evO4xb6jm',
        'Connecticut': '37i9dQZF1DZ06evO2dO1kA', #Moby
        'Connecticut'.casefold(): '37i9dQZF1DZ06evO2dO1kA',
        'Delaware': '37i9dQZF1DZ06evO0D9jr4', #George Thorogood
        'Delaware'.casefold(): '37i9dQZF1DZ06evO0D9jr4',
        'Florida': '37i9dQZF1DX1PfYnYcpw8w', #Ariana Grande
        'Florida'.casefold(): '37i9dQZF1DX1PfYnYcpw8w',
        'Georgia': '37i9dQZF1DZ06evO0FPX4A', #Ray Charles
        'Georgia'.casefold(): '37i9dQZF1DZ06evO0FPX4A',
        'Hawaii': '37i9dQZF1DZ06evO03DwPK', #Bruno Mars
        'Hawaii'.casefold(): '37i9dQZF1DZ06evO03DwPK',
        'Idaho': '37i9dQZF1DZ06evO1L4rwW', #Paul Revere
        'Idaho'.casefold(): '37i9dQZF1DZ06evO1L4rwW',
        'Illinois': '37i9dQZF1DZ06evO3nMr04', #Kanye West
        'Illinois'.casefold(): '37i9dQZF1DZ06evO3nMr04',
        'Indiana': '37i9dQZF1DZ06evO1SVXaM', #Michael Jackson
        'Indiana'.casefold(): '37i9dQZF1DZ06evO1SVXaM',
        'Iowa': '37i9dQZF1DZ06evNZYGncI', #Slipknot
        'Iowa'.casefold(): '37i9dQZF1DZ06evNZYGncI',
        'Kansas': '37i9dQZF1DZ06evO2e9Kc8', #Martina McBride
        'Kansas'.casefold(): '37i9dQZF1DZ06evO2e9Kc8',
        'Kentucky': '37i9dQZF1DZ06evO0VT8cA', #Loretta Lynn
        'Kentucky'.casefold: '37i9dQZF1DZ06evO0VT8cA',
        'Louisiana': '37i9dQZF1DZ06evO0Co11u', #Louis Armstrong
        'Louisiana'.casefold(): '37i9dQZF1DZ06evO0Co11u',
        'Maine': '37i9dQZF1DZ06evO048Spq', #Howie Day
        'Maine'.casefold(): '37i9dQZF1DZ06evO048Spq',
        'Maryland': '37i9dQZF1DZ06evO17hgFa', #Billie Holiday
        'Maryland'.casefold(): '37i9dQZF1DZ06evO17hgFa',
        'Massachusetts': '37i9dQZF1DZ06evO4x3X2w', #Aerosmith
        'Massachusetts'.casefold(): '37i9dQZF1DZ06evO4x3X2w',
        'Michigan': '37i9dQZF1DZ06evO4iAGsg', #Stevie Wonder
        'Michigan'.casefold(): '37i9dQZF1DZ06evO4iAGsg',
        'Minnesota': '37i9dQZF1DZ06evO3262Tm', #Prince
        'Minnesota'.casefold(): '37i9dQZF1DZ06evO3262Tm',
        'Mississippi': '37i9dQZF1DZ06evO2n9pny', #Elvis Presley
        'Mississippi'.casefold(): '37i9dQZF1DZ06evO2n9pny',
        'Missouri': '37i9dQZF1DZ06evO1dAid2', #Chuck Berry
        'Missouri'.casefold(): '37i9dQZF1DZ06evO1dAid2',
        'Montana': '37i9dQZF1E4r7R3SxrJrA4', #Jeff Ament
        'Montana'.casefold(): '37i9dQZF1E4r7R3SxrJrA4',
        'Nebraska': '37i9dQZF1DZ06evO1IUGmB', #Conor Oberst
        'Nebraska'.casefold(): '37i9dQZF1DZ06evO1IUGmB',
        'Nevada': '37i9dQZF1E4sev34rkHhqe', #Brandon Flowers
        'Nevada'.casefold(): '37i9dQZF1E4sev34rkHhqe',
        'New Hampshire': '37i9dQZF1DZ06evO3V4b3a', #Ray LaMontagne
        'New Hampshire'.casefold(): '37i9dQZF1DZ06evO3V4b3a',
        'New Jersey': '37i9dQZF1DZ06evO476tMI', #Whitney Houston
        'New Jersey'.casefold(): '37i9dQZF1DZ06evO476tMI',
        'New Mexico': '37i9dQZF1DZ06evO43Szeg', #Demi Lovato
        'New Mexico'.casefold(): '37i9dQZF1DZ06evO43Szeg',
        'New York': '37i9dQZF1DZ06evO3SPjlS', #Billy Joel
        'New York'.casefold(): '37i9dQZF1DZ06evO3SPjlS',
        'North Carolina': '37i9dQZF1DX8OYzU0lx5hL', #Nina Simone
        'North Carolina'.casefold(): '37i9dQZF1DX8OYzU0lx5hL',
        'North Dakota': '37i9dQZF1DZ06evO3xnLSU', #Peggy Lee
        'North Dakota'.casefold(): '37i9dQZF1DZ06evO3xnLSU',
        'Ohio': '37i9dQZF1DZ06evO3gxo8o', #John Legend
        'Ohio'.casefold(): '37i9dQZF1DZ06evO3gxo8o',
        'Oklahoma': '5hArM20WmQt5ZoUEN5gA9z', #Garth Brooks
        'Oklahoma'.casefold(): '5hArM20WmQt5ZoUEN5gA9z',
        'Oregon': '37i9dQZF1DZ06evO1u2tEI', #Elliott Smith
        'Oregon'.casefold(): '37i9dQZF1DZ06evO1u2tEI',
        'Pennsylvania': '37i9dQZF1DX5KpP2LN299J', #Taylor Swift
        'Pennsylvania'.casefold(): '37i9dQZF1DX5KpP2LN299J',
        'Rhode Island': '37i9dQZF1DZ06evO1W4Gvx', #Nelson Eddy
        'Rhode Island'.casefold(): '37i9dQZF1DZ06evO1W4Gvx',
        'South Carolina': '37i9dQZF1DZ06evO4y2rNC', #James Brown
        'South Carolina'.casefold(): '37i9dQZF1DZ06evO4y2rNC',
        'South Dakota': '37i9dQZF1DZ06evO0nhqNT', #Shawn Colvin
        'South Dakota'.casefold(): '37i9dQZF1DZ06evO0nhqNT',
        'Tennessee': '37i9dQZF1DZ06evO1KXgbK', #Dolly Parton
        'Tennessee'.casefold(): '37i9dQZF1DZ06evO1KXgbK',
        'Texas': '37i9dQZF1DZ06evO3v06CA', #Willie Nelson
        'Texas'.casefold(): '37i9dQZF1DZ06evO3v06CA',
        'Utah': '37i9dQZF1DZ06evO1v5MdV', #David Archuleta
        'Utah'.casefold(): '37i9dQZF1DZ06evO1v5MdV',
        'Vermont': '37i9dQZF1DZ06evO11Xz1u', #Grace Potter
        'Vermont'.casefold(): '37i9dQZF1DZ06evO11Xz1u',
        'Virginia': '37i9dQZF1DZ06evO1rPgfC', #Missy Elliott
        'Virginia'.casefold(): '37i9dQZF1DZ06evO1rPgfC',
        'Washington': '37i9dQZF1DZ06evO4cWDcc', #Jimi Hendrix
        'Washington'.casefold(): '37i9dQZF1DZ06evO4cWDcc',
        'West Virginia': '37i9dQZF1DZ06evO0zdG6s', #Brad Paisley
        'West Virginia'.casefold(): '37i9dQZF1DZ06evO0zdG6s',
        'Wisconsin': '37i9dQZF1DZ06evO1iz8xP', #Les Paul
        'Wisconsin'.casefold(): '37i9dQZF1DZ06evO1iz8xP',
        'Wyoming': '37i9dQZF1DZ06evO2MsJSe', #Chris LeDoux
        'Wyoming'.casefold(): '37i9dQZF1DZ06evO2MsJSe'
    }
   
    return singers_by_state.get(state, 'Singer not found for this state')


