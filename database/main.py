from create_tables import create_tables
from database.create_table_young_animals import create_table_young_animals
from database.delete_camels import delete_data
from database.union_all_tables import create_table_for_all_animals
from insert_data_in_table_pets import insert_data_into_table_pets
from insert_data_in_table_pack_animals import insert_data_into_table_pack_animal


def main():
    create_tables()
    insert_data_into_table_pets()
    insert_data_into_table_pack_animal()
    delete_data()
    create_table_young_animals()
    create_table_for_all_animals()


if __name__ == '__main__':
    main()
