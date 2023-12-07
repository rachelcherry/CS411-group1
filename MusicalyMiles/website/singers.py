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
        'Illinois': 'Kanye West', #Kanye West
        'Illinois'.casefold(): 'Kanye West',
        'Indiana': 'Michael Jackson', #Michael Jackson
        'Indiana'.casefold(): 'Michael Jackson',
        'Iowa': 'Slipknot', #Slipknot
        'Iowa'.casefold(): 'Slipknot',
        'Kansas': 'Martina McBride', #Martina McBride
        'Kansas'.casefold(): 'Martina McBride',
        'Kentucky': 'Loretta Lynn', #Loretta Lynn
        'Kentucky'.casefold: 'Loretta Lynn',
        'Louisiana': 'Louis Armstrong', #Louis Armstrong
        'Louisiana'.casefold(): 'Louis Armstrong',
        'Maine': 'Howie Day', #Howie Day
         'Maine'.casefold(): 'Howie Day',
        'Maryland': 'Billie Holiday', #Billie Holiday
        'Maryland'.casefold(): 'Billie Holiday',
        'Massachusetts': 'Aerosmith', #Aerosmith
        'Massachusetts'.casefold(): 'Aerosmith',
        'Michigan': 'Stevie Wonder', #Stevie Wonder
        'Michigan'.casefold(): 'Stevie Wonder',
        'Minnesota': 'Prince', #Prince
        'Minnesota'.casefold(): 'Prince',
        'Mississippi': 'Elvis Presley', #Elvis Presley
        'Mississippi'.casefold(): 'Elvis Presley',
        'Missouri': 'Chuck Berry', #Chuck Berry
        'Missouri'.casefold(): 'Chuck Berry',
        'Montana': 'Jeff Ament', #Jeff Ament
        'Montana'.casefold(): 'Jeff Ament',
        'Nebraska': 'Conor Oberst', #Conor Oberst
        'Nebraska'.casefold(): 'Conor Oberst',
        'Nevada': 'Brandon Flowers', #Brandon Flowers
        'Nevada'.casefold(): 'Brandon Flowers',
        'New Hampshire': 'Ray LaMontagne', #Ray LaMontagne
        'New Hampshire'.casefold(): 'Ray LaMontagne',
        'New Jersey': 'Whitney Houston', #Whitney Houston
        'New Jersey'.casefold(): 'Whitney Houston',
        'New Mexico': 'Demi Lovato', #Demi Lovato
        'New Mexico'.casefold(): 'Demi Lovato',
        'New York': 'Billy Joel', #Billy Joel
        'New York'.casefold(): 'Billy Joel',
        'North Carolina': 'Nina Simone', #Nina Simone
        'North Carolina'.casefold(): 'Nina Simone',
        'North Dakota': 'Peggy Lee', #Peggy Lee
        'North Dakota'.casefold(): 'Peggy Lee',
        'Ohio': 'John Legend', #John Legend
        'Ohio'.casefold(): 'John Legend',
        'Oklahoma': 'Garth Brooks', #Garth Brooks
        'Oklahoma'.casefold(): 'Garth Brooks',
        'Oregon': 'Elliott Smith', #Elliott Smith
        'Oregon'.casefold(): 'Elliott Smith',
        'Pennsylvania': 'Taylor Swift', #Taylor Swift
        'Pennsylvania'.casefold(): 'Taylor Swift',
        'Rhode Island': 'Nelson Eddy', #Nelson Eddy
        'Rhode Island'.casefold(): 'Nelson Eddy',
        'South Carolina': 'James Brown', #James Brown
        'South Carolina'.casefold(): 'James Brown',
        'South Dakota': 'Shawn Colvin', #Shawn Colvin
        'South Dakota'.casefold(): 'Shawn Colvin',
        'Tennessee': 'Dolly Parton', #Dolly Parton
        'Tennessee'.casefold(): 'Dolly Parton',
        'Texas': 'Willie Nelson', #Willie Nelson
        'Texas'.casefold(): 'Willie Nelson',
        'Utah': 'David Archuleta', #David Archuleta
        'Utah'.casefold(): 'David Archuleta',
        'Vermont': 'Grace Potter', #Grace Potter
        'Vermont'.casefold(): 'Grace Potter',
        'Virginia': 'Missy Elliott', #Missy Elliott
        'Virginia'.casefold(): 'Missy Elliott',
        'Washington': 'Jimi Hendrix', #Jimi Hendrix
        'Washington'.casefold(): 'Jimi Hendrix',
        'West Virginia': 'Brad Paisley', #Brad Paisley
        'West Virginia'.casefold(): 'Brad Paisley',
        'Wisconsin': 'Les Paul', #Les Paul
        'Wisconsin'.casefold(): 'Les Paul',
        'Wyoming': 'Chris LeDoux', #Chris LeDoux
        'Wyoming'.casefold(): 'Chris LeDoux'
    }
   
    return singers_by_state.get(state, 'Singer not found for this state')


