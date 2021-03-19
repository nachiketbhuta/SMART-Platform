// import { MutationTree } from "vuex";
// import { getAccessorType } from "nuxt-typed-vuex";

// interface loginUserInfo {
//     user: Object;
//     token: string;
//     credential: Object;
// }
// export type RootState = ReturnType<typeof state>;

// export const state = () => ({
//     userInfo: {
//         user: {},
//         token: "",
//         credential: {}
//     }
// });

// export const mutations: MutationTree<RootState> = {
//     loginUser(state, payload: loginUserInfo) {
//         state.userInfo.user = payload.user;
//         state.userInfo.token = payload.token;
//         state.userInfo.credential = payload.credential;
//     },
//     setUser(state, payload: Object) {
//         state.userInfo.user = payload;
//     }
// };

// export const accessorType = getAccessorType({
//     state,
//     mutations
// });
