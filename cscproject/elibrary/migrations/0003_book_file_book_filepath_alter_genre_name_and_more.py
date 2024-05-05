# Generated by Django 4.0.8 on 2024-04-28 16:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('elibrary', '0002_alter_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(default=datetime.datetime(2024, 4, 28, 16, 48, 21, 557241, tzinfo=utc), upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='filepath',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(choices=[('Algorithms', 'Algorithms'), ('Data Structures', 'Data Structures'), ('Programming Languages', 'Programming Languages'), ('Databases', 'Databases'), ('Networking', 'Networking'), ('Operating Systems', 'Operating Systems'), ('Software Engineering', 'Software Engineering'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Machine Learning', 'Machine Learning'), ('Computer Vision', 'Computer Vision'), ('Natural Language Processing', 'Natural Language Processing'), ('Computer Graphics', 'Computer Graphics'), ('Human-Computer Interaction', 'Human-Computer Interaction'), ('Cybersecurity', 'Cybersecurity'), ('Web Development', 'Web Development'), ('Mobile Development', 'Mobile Development'), ('Cloud Computing', 'Cloud Computing'), ('Big Data', 'Big Data'), ('Internet of Things', 'Internet of Things'), ('Blockchain', 'Blockchain'), ('Quantum Computing', 'Quantum Computing'), ('Bioinformatics', 'Bioinformatics'), ('Computational Biology', 'Computational Biology'), ('Robotics', 'Robotics'), ('Game Development', 'Game Development'), ('Embedded Systems', 'Embedded Systems'), ('High-Performance Computing', 'High-Performance Computing'), ('Distributed Systems', 'Distributed Systems'), ('Parallel Computing', 'Parallel Computing'), ('Computational Mathematics', 'Computational Mathematics'), ('Computational Physics', 'Computational Physics'), ('Scientific Computing', 'Scientific Computing'), ('Computer Science Education', 'Computer Science Education'), ('Others', 'Others')], max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(choices=[('Algorithms', 'Algorithms'), ('Data Structures', 'Data Structures'), ('Computer Networks', 'Computer Networks'), ('Database Systems', 'Database Systems'), ('Operating Systems', 'Operating Systems'), ('Software Engineering', 'Software Engineering'), ('Programming Languages', 'Programming Languages'), ('Web Development', 'Web Development'), ('Machine Learning', 'Machine Learning'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Computer Vision', 'Computer Vision'), ('Natural Language Processing', 'Natural Language Processing'), ('Big Data', 'Big Data'), ('Cloud Computing', 'Cloud Computing'), ('Cybersecurity', 'Cybersecurity'), ('Blockchain', 'Blockchain'), ('Internet of Things', 'Internet of Things'), ('Robotics', 'Robotics'), ('Human-Computer Interaction', 'Human-Computer Interaction'), ('Computer Graphics', 'Computer Graphics'), ('Embedded Systems', 'Embedded Systems'), ('Mobile Computing', 'Mobile Computing'), ('Game Development', 'Game Development'), ('Bioinformatics', 'Bioinformatics'), ('Quantum Computing', 'Quantum Computing'), ('Computer Architecture', 'Computer Architecture'), ('Parallel Computing', 'Parallel Computing'), ('Distributed Systems', 'Distributed Systems'), ('Compiler Design', 'Compiler Design'), ('Software Testing', 'Software Testing'), ('DevOps', 'DevOps'), ('Agile Methodologies', 'Agile Methodologies'), ('UI/UX Design', 'UI/UX Design'), ('Data Science', 'Data Science'), ('Computer Ethics', 'Computer Ethics'), ('Digital Forensics', 'Digital Forensics'), ('Computer Crime', 'Computer Crime'), ('Computer Vision', 'Computer Vision'), ('Ethical Hacking', 'Ethical Hacking'), ('Virtual Reality', 'Virtual Reality'), ('Augmented Reality', 'Augmented Reality'), ('Network Security', 'Network Security'), ('Software Development', 'Software Development'), ('Computer Hardware', 'Computer Hardware'), ('Information Retrieval', 'Information Retrieval'), ('Information Security', 'Information Security'), ('Cloud Security', 'Cloud Security'), ('Cryptography', 'Cryptography'), ('Data Mining', 'Data Mining'), ('Pattern Recognition', 'Pattern Recognition'), ('Image Processing', 'Image Processing'), ('Simulation', 'Simulation'), ('Computer Algebra', 'Computer Algebra'), ('Computational Geometry', 'Computational Geometry'), ('Computer Vision', 'Computer Vision'), ('Expert Systems', 'Expert Systems'), ('Automated Reasoning', 'Automated Reasoning'), ('Computer Algebra Systems', 'Computer Algebra Systems'), ('Computer-aided Design', 'Computer-aided Design'), ('Computer-aided Manufacturing', 'Computer-aided Manufacturing'), ('Computer-based Training', 'Computer-based Training'), ('Computer-assisted Instruction', 'Computer-assisted Instruction'), ('Interactive Learning', 'Interactive Learning'), ('Computer-based Testing', 'Computer-based Testing'), ('Computer Science Education', 'Computer Science Education'), ('Online Learning', 'Online Learning'), ('Distance Education', 'Distance Education'), ('E-Learning', 'E-Learning'), ('Blended Learning', 'Blended Learning'), ('Mobile Learning', 'Mobile Learning'), ('Virtual Learning Environment', 'Virtual Learning Environment'), ('Learning Management System', 'Learning Management System'), ('Educational Technology', 'Educational Technology'), ('Instructional Design', 'Instructional Design'), ('Educational Games', 'Educational Games'), ('Serious Games', 'Serious Games'), ('Gamification', 'Gamification'), ('Computer-mediated Communication', 'Computer-mediated Communication'), ('Online Collaboration', 'Online Collaboration'), ('Computer-supported Cooperative Work', 'Computer-supported Cooperative Work'), ('Groupware', 'Groupware'), ('Social Media', 'Social Media'), ('Social Networking', 'Social Networking'), ('Online Communities', 'Online Communities'), ('Virtual Communities', 'Virtual Communities'), ('Computer-based Social Network Analysis', 'Computer-based Social Network Analysis'), ('Online Social Networks', 'Online Social Networks'), ('Social Computing', 'Social Computing'), ('Computer-supported Collaborative Learning', 'Computer-supported Collaborative Learning'), ('Computer-aided Assessment', 'Computer-aided Assessment'), ('Digital Libraries', 'Digital Libraries'), ('Library Automation', 'Library Automation'), ('Library Management Systems', 'Library Management Systems'), ('Library Information Systems', 'Library Information Systems'), ('Information Literacy', 'Information Literacy'), ('Library Instruction', 'Library Instruction'), ('Library Research', 'Library Research'), ('Library Resources', 'Library Resources'), ('Library Services', 'Library Services'), ('Library Catalogs', 'Library Catalogs'), ('Library Cataloging', 'Library Cataloging'), ('Library Classification', 'Library Classification'), ('Library Collection Development', 'Library Collection Development'), ('Library Holdings', 'Library Holdings'), ('Library Preservation', 'Library Preservation'), ('Library Digitization', 'Library Digitization'), ('Library Archives', 'Library Archives'), ('Library Special Collections', 'Library Special Collections'), ('Library Rare Books', 'Library Rare Books'), ('Library Manuscripts', 'Library Manuscripts'), ('Library Periodicals', 'Library Periodicals'), ('Library Serials', 'Library Serials'), ('Library Journals', 'Library Journals'), ('Library Magazines', 'Library Magazines'), ('Library Newspapers', 'Library Newspapers'), ('Library Reference', 'Library Reference'), ('Library Information Retrieval', 'Library Information Retrieval'), ('Library Reference Services', 'Library Reference Services'), ('Library User Services', 'Library User Services'), ('Library Circulation', 'Library Circulation'), ('Library Interlibrary Loan', 'Library Interlibrary Loan'), ('Library Document Delivery', 'Library Document Delivery'), ('Library Electronic Resources', 'Library Electronic Resources'), ('Library E-books', 'Library E-books'), ('Library E-journals', 'Library E-journals'), ('Library Online Databases', 'Library Online Databases'), ('Library Digital Resources', 'Library Digital Resources'), ('Library Institutional Repositories', 'Library Institutional Repositories'), ('Library Digital Archives', 'Library Digital Archives'), ('Library Digital Preservation', 'Library Digital Preservation'), ('Library Metadata', 'Library Metadata'), ('Library Linked Data', 'Library Linked Data'), ('Library Semantic Web', 'Library Semantic Web'), ('Library Open Access', 'Library Open Access'), ('Library Scholarly Communication', 'Library Scholarly Communication'), ('Library Publishing', 'Library Publishing'), ('Library Peer Review', 'Library Peer Review'), ('Library Research Data Management', 'Library Research Data Management'), ('Library Bibliometrics', 'Library Bibliometrics'), ('Library Citation Analysis', 'Library Citation Analysis'), ('Library Information Literacy', 'Library Information Literacy'), ('Library Digital Literacy', 'Library Digital Literacy'), ('Library Media Literacy', 'Library Media Literacy'), ('Library Visual Literacy', 'Library Visual Literacy')], max_length=50),
        ),
    ]
