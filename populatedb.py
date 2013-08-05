#-*- coding: UTF-8-*-
from app import models, db

#Add categories
cat1 = models.Category(category_name="Arab Crossroads")
cat2 = models.Category(category_name="Film and New Media")
cat3 = models.Category(category_name="Chemistry")
cat4 = models.Category(category_name="Computer Science")
cat5 = models.Category(category_name="Core")
cat6 = models.Category(category_name="Economics")
cat7 = models.Category(category_name="Engineering")
cat8 = models.Category(category_name="History")
cat9 = models.Category(category_name="Mathematics")
cat10 = models.Category(category_name="Music")
cat11 = models.Category(category_name="Philosophy")
cat12 = models.Category(category_name="Physics")
cat13 = models.Category(category_name="Political")
cat14 = models.Category(category_name="Psychology")
cat15 = models.Category(category_name="Social Research and Public Policy")
cat16 = models.Category(category_name="Theater")
cat17 = models.Category(category_name="Visual Arts")
cat18 = models.Category(category_name="Litterature and Creative Writing")
cat19 = models.Category(category_name="Biology")
cat20 = models.Category(category_name="Language")

db.session.add_all([cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10,\
                   cat11, cat12, cat13, cat14, cat15, cat16, cat17, cat18, cat19, cat20])

db.session.commit()



prof_list = ['Brenda Abdelall', 'Rahma Abdulkadir', 'Jennifer Acker', 'Stefan Agamanolis', 'Rana Al-Assah', 'Tarek Al-Ghoussein', 'Muhamed Al-Khalil', \
             'Diogo Almeida', 'Jose Alvarez', 'Yasser Alwan', 'Awam Ampka', 'Alexandra Avakian', 'Marzia Balzani', 'Rachel Barkow', 'Mohamad Bazzi', 'Peter Bearman',\
             'Florent Benaych-Georges', 'Julien Berestycki', 'Joel Bernstein', 'Bruno Biais', 'Florin Bilbiie', 'Alberto Bisin', 'Ned Block', 'Anna Bogomolnaia',\
             'Sofiane Bouarroudj', 'Saglar Bougdaeva', 'Francois Bourguignon', 'Jesse Bransford', 'Hannah Bruckner', 'Cristina Buarque de Hollanda', 'Bruce Buchanan',\
             'John Burt', 'David Cai', 'Federico Camia', 'Susan Carey', 'David Cesarini', 'Mario Chacon', 'Kanchan Chandra', 'Celina Charlier', 'Jean-Francois Chassagneux',\
             'Una Chaudhuri', 'Jay Chen', 'Annia Ciezadlo', 'Jules Coleman', 'Douglas Cook', 'Scandar Copti', 'Catherine Coray', 'Martin Daughtry', 'Chetan Dave',\
             'Georgi Derluguian', 'Claude Desplan', 'Alexandra Dimitri', 'Jo Dixon', 'Georges Djouma', 'Tim Dore', 'Omima El Araby', 'Abdulmotaleb El Saddik', 'Jed Emerson',\
             'Paula England', 'Tzipora Eynot', 'Defne Ezgi', 'Reindert Falkenburg', 'Walter Feldman', 'Scott Fitzgerald', 'Roger Friedland', 'Joseph Gelfand', 'Carl Gladish',\
             'Carlos Guedes', 'Christian Haefke', 'Bernard Haykel', 'Peter Hedstrom', 'Leonard Helmrich', 'PJ Henry', 'Simon Hix', 'Stephen Holmes', 'Paulo Horta', \
             'Dale Hudson', 'Jean Imbs', 'Nasser Isleem', 'Ramesh Jagannathan', 'Tala Jarjour', 'Jeffrey Jensen', 'Seung-Hoon Jeong', 'Xiao Jiao', 'Philip Kennedy', \
             'Sachin Khapli',\
             'Jason King', 'Khulood Kittaneh', 'Perri Klass', 'Martin Klimke', 'Eric Klinenberg', 'Hans-Dieter Klingermann', 'Brian Koss', 'Joseph Koussa', 'Anthony Kronman',\
             'Kevin Kuhlke', 'Sunil Kumar', 'Michael Laver', 'Yves Le-Jan', 'John Leahy', 'Debra Levine', 'Mazin Magzoub', 'Sheetal Majithia', 'Charlie Major', 'Samreen Malik',\
             'Jeff Manza', 'Timothy Maudlin', 'Laura Mayoral', 'David McGlennon', 'Pascal Menoret', 'Marc Michael', 'Maximilian Mihm', 'Judith Miller', 'Lauren Minsky', \
             'Amir Minsky', 'Phil Mitsis', 'Ann Morning', 'Rebecca Morton', 'Herve Moulin', 'Pance Naumov', 'Wolfgang Neuber', 'Abdul Noury', 'Yaw Nyarko', 'Sana Odeh', \
             'Mo Ogrodnik', 'John OBrien', 'Christopher Paik', 'Robert Parthesius', 'Cyrus Patell', 'Nathalie Peutz', 'Fabio Piano', 'Ruben Polendo', 'Goffredo Puccetti',\
             'Michael Purugganan', 'Jean-Renaud Pycke', 'Susanne Quadflieg', 'Matthew Quayle', 'Wael Rabeh', 'Adam Ramey', 'Romain Ranciere', 'Debraj Ray', 'Kevin Riordan',\
             'Mallory Roberts', 'Nadine Roth', 'Gilles Saint-Paul', 'Kourosh Salehi-Ashtiani', 'Lamar Sanders', 'Joanne Savio', 'Jim Savio', 'David Scicchitano', 'Gail Segal',\
             'John Sexton', 'Nishi Shah', 'Qiuxia Shao', 'Azim Shariff', 'Dennis Shasha', 'Daniel Shiffman', 'Ella Shohat', 'Matthew Silverstein', 'Ozgur Sinanoglu',\
             'Clifford Siskin', 'Sandra Sissel', 'Ahna Skop', 'Shafer Smith', 'Roy Smith', 'Katepalli Sreenivasan', 'Heidi Stalla', 'Robert Stam', 'Justin Stearns',\
             'Catharine Stimpson', 'Rajeswari Sunder Rajan', 'Mark Swislocki', 'Ivan Szelenyi', 'Ignatius Tan', 'Kevin Thom', 'Florencia Torche', 'John Torreano',\
             'Godfried Toussaint', 'Ali Trabolsi', 'James Traub', 'Kiryl Tsishchanka', 'Joshua Tucker', 'Thierry Verdier', 'Tyler Volk', 'Joanna Waley-Cohen', 'John Waterbury',\
             'Bryan Waterman', \
             'Niobe Way', 'Mariet Westermann', 'Deborah Williams', 'Charles Wilson', 'Larry Wolff', 'Caitlin Zaloom', 'Shamoon Zamir', 'Ingyin Zaw', 'Jonathan Zimmerman',\
             'Edward Ziter', 'James Zogby']
#Add professors
for i in range(198):                 
    prof= models.Professor(professor_name = prof_list[i])
    db.session.add(prof)

db.session.commit()

# some users:

user2 =models.User(net_id="tpn223")
user3 =models.User(net_id="mji237")
user4 =models.User(net_id="mdk353")
user5 =models.User(net_id="mtk297")


db.session.add_all([user2, user3, user4, user5])



db.session.commit()

#Add courses

course1 = models.Course(course_name="Anthropology and the Arab World"\
        , course_description= "How have anthropologists encountered,\
        written about, and produced the 'Arab world' over the past century?\
        Beginning with early Western travelers' imaginaries of Arabia and\
        ending with an ethnography of Egyptian dreamscapes, this course\
        provides an introduction to the anthropological project and to the\
        everyday realities of people living in the region. Through\
        ethnography, literature, film, and field trips, we explore such topics\
        as colonialism, nation building and development, family, gender and\
        piety, media, art and globalization, labor migration, diaspora, and\
        pilgrimage." )

course2 = models.Course(course_name="What is Music?",
course_description= "This course analyzes what we understand as\
'music.' Drawing on music of different styles from all over the world,\
we will explore what constitutes musical meaning, how it is produced,\
and how music expresses feelings. Taking advantage of the\
multicultural nature of NYUAD, we will explore the cultural and\
universal mechanisms at play when we listen and understand music. A\
lab portion of the class guides students through basic musical\
elements such as notation systems, scales, and simple compositional\
techniques.")


course3 = models.Course(course_name="Innovation in the Ancient World",
course_description="This course probes the heuristics of human\
innovation in the ancient world. We study the earliest human\
inventions such as spears and simple tools; ponder the methods that\
might have been used in the construction of monolithic structures such\
as Stone Henge, Egyptian obelisks, and pyramids; and explore examples\
of technological innovations that affected the course of human\
history. Throughout the course, the emphasis is on developing personal\
approaches to creativity and innovation by studying specific examples\
of these attributes from the ancient world.")



course4 =models.Course(course_name="Bio Imaging", course_description="This course presents an introduction to image\
formation, processing, and related techniques, as they pertain to imaging of biological structures for medical and other\
 applications. Ultrasound, Magnetic Resonance Imaging, X-Ray Tomography, and Nuclear Medicine are among the topics cover\
ed, together with a hands-on introduction to biomedical image processing and pattern recognition.")

db.session.add_all([course1, course2, course3, course4])

db.session.commit()






