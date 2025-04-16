from create_tables import create_tables
from insert_data_in_table_pets import insert_data_into_table_pets
from insert_data_in_table_pack_animals import insert_data_into_table_pack_animal


def main():
    create_tables()
    insert_data_into_table_pets()
    insert_data_into_table_pack_animal()


if __name__ == '__main__':
    main()
