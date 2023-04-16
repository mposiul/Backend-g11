import { Router } from "express";
import { actualizarProducto, crearProducto, devolverProducto, listarProductos } from "../controllers/productos.controller.js";

export const productoRouter = Router();

productoRouter.route('/productos').post(crearProducto).get(listarProductos)
// productoRouter.post("/productos", crearProducto);
//productoRouter.get("/productos", listarProductos);

//productoRouter.get("/producto/:id", devolverProducto);
productoRouter.route("/producto/:id").get(devolverProducto).patch(actualizarProducto).put(actualizarProducto)
