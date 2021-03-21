import { GetterTree, MutationTree } from "vuex";
import infy_monthly from "@/utils/INFY_MONTHLY.json";

export const state = () => ({
    email: "",
    displayName: "",
    token: "",
    pageTitle: "Commercio",
    watchlist: [],
    alpha_api_key: "GMF5WJDMLV73230F",
    api_url: "localhost:8000",
    stockData: []
});

export type RootState = ReturnType<typeof state>;

export const getters: GetterTree<RootState, RootState> = {
    // @ts-ignore
    email: state => state.email,
    // @ts-ignore
    displayName: state => state.displayName,
    token: state => state.token,
    pageTitle: state => state.pageTitle,
    watchlist: state => state.watchlist,
    alpha_api_key: state => state.alpha_api_key,
    api_url: state => state.api_url,
    stockData: state => state.stockData,
};

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
    setPageTitle(state, payload) {
        state.pageTitle = payload;
    },
    setWatchlist(state, payload) {
        state.watchlist = payload;
    },
    setStockData(state, payload) {
        state.stockData = payload;
    }
};
