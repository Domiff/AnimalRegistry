select_query_pets = (
                "SELECT * FROM Pets "
                "WHERE TIMESTAMPDIFF(YEAR, Pets.date_birth, CURDATE()) >= 1 "  
                "AND TIMESTAMPDIFF(YEAR, Pets.date_birth, CURDATE()) < 3;"
                )


select_query_pack_animals = """
                SELECT * FROM PackAnimals 
                WHERE TIMESTAMPDIFF(YEAR, PackAnimals.date_birth, CURDATE()) >= 1 
                AND TIMESTAMPDIFF(YEAR, PackAnimals.date_birth, CURDATE()) < 3;
                """
