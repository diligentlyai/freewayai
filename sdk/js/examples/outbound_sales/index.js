"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
require('dotenv').config();
const index_js_1 = __importDefault(require("../../dist/index.js"));
const dd = new index_js_1.default();
const NEW_PROFILE_LOCATION = "data/new_profile_data.json";
const PROFILES_AND_MESSAGES_LOCATION = "data/profiles_and_messages.json";
// async function get_new_message (message: string) {
//     return 'A Message';
// }
console.log('Here');
