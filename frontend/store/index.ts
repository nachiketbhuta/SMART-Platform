import { GetterTree, MutationTree } from "vuex";

export const state = () => ({
    email: "",
    displayName: "",
    token: ""
});

export type RootState = ReturnType<typeof state>;

export const getters: GetterTree<RootState, RootState> = {
    // @ts-ignore
    email: state => state.email,
    // @ts-ignore
    displayName: state => state.displayName,
    token: state => state.token
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
    }
};

