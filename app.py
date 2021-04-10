import numpy as np
import streamlit as st
from utils.data_structures import Graph, MinHeap
from utils.datagen import DataGenerator

st.set_page_config(page_title='Shelby')

def main():
    """Main function of the app"""
    st.sidebar.title("About")

    st.sidebar.info(
        "This project is for educational purposes only and is licensed under the MIT license. Copyright (c) 2020 Lucas Leonardo, Wesley Alves"
    )
    st.sidebar.info(
        "Dataset fornecido por John Burkardt, do Departamento de Computação Cientifica - Florida State University. Você pode baixar os dados [aqui](https://people.sc.fsu.edu/~jburkardt/datasets/cities/cities.html)"
    )

    st.title('Shelby | Personal persuasion assistant')
    st.write("**Original dataset description:**")

    st.write("This directed network was created from a survey that took place in 1994/1995. Each student was asked to list his 5 best female and his 5 male friends. A node represents a student and an edge between two students shows that the left student chose the right student as a friend. Higher edge weights indicate more interactions and a edge weight shows that there is no common activity at all.")

    st.write("**Personalized problem statement:**")
    st.write("Amanda, a big fan of the art of persuasion, wanted to discover the most efficient way to manipulate two people A and B, in order to ensure that they act the way she wants.")
    st.write("As Amanda is a training statistician, she carried out a causality study and realized that, given two people A and B, the best way to manipulate them is by looking for the weakest connection chain between them and trying to persuade them collectively.")
    st.write("The moment of selection for the exchange is coming and, in those moments, to be well regarded by the faculty is essential. In this way, Amanda is 100% determined to, if necessary, manipulate all people in college. So she created a system that indicates the weakest link between two people.")
    st.write("This system, in addition to returning the strength of the link, also returns the ID of the people it needs to act in addition to the two chosen.")
    st.write("It is important to note that the order of influence matters. If X has connection strength 3 with Y, it does not mean that Y also has connection strength 3 with X. Therefore, for the strategy to work, Amanda needs to follow the order indicated by Shelby perfectly.")
    
    st.subheader('Select the two IDs:')

    datagen = DataGenerator('src/data.tsv')
    adjacency_list, n = datagen.get_data()
    cities_network = Graph(adjacency_list, n)

    id1 = st.selectbox(options=list(range(1, n)), label='First ID')
    id2 = st.selectbox(options=list(range(1, n)), label='Second ID')

    if st.button('Find the weakest link between the two people:'):
        dist, path = cities_network.minimal_path(id1, id2)
        if dist == np.inf:
            st.error(f"There is no possible link between {id1} and {id2}.")
        elif dist == 0:
            st.error("Please, select two different IDs.")
        else:
            st.success(f'The strength of the weaker link between {id1} and {id2} is {dist}.')
            st.success(f"You should manipulate: {'→'.join(path)}")

if __name__ == "__main__":
    main()