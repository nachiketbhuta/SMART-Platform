import { GetterTree, MutationTree } from "vuex";

export const state = () => ({
    email: "",
    displayName: "",
    token: "",
    pageTitle: "Commercio"
});

export type RootState = ReturnType<typeof state>;

export const getters: GetterTree<RootState, RootState> = {
    // @ts-ignore
    email: state => state.email,
    // @ts-ignore
    displayName: state => state.displayName,
    token: state => state.token,
    pageTitle: state => state.pageTitle
}

export const mutations: MutationTree<RootState> = {
    setEmail(state, payload) {
        state.email = payload;
    },
    setDisplayName(state, payload) {
        state.displayName = payload;
    },
    setToken(state, payload) {
        state.token = payload;
    },
    setPageTitle(state, payload){
        state.pageTitle = payload
    }
};

