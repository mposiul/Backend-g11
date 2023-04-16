import { Prisma } from "../prisma.js";

export const crearProducto = async (req, res) => {
    const data = req.body;

    // SELECT id FROM categorias WHERE id = ....;

    // TODO: Validar si la categoria en la cual se quiere crear el producto no este desabilitada
    const categoria = await Prisma.categoria.findFirst({
        where: { id: data.categoriaId },
        select: { id: true },
    });

    if (!categoria) {
        return res.status(400).json({
            message: "Categoria no existe",
        });
    }

    try {
        const nuevoProducto = await Prisma.producto.create({
            data: {
                ...data,
                fechaVencimiento: new Date(data.fechaVencimiento),
            },
        });

        return res.status(201).json({
            message: "Producto creado exitosamente",
            content: nuevoProducto,
        });
    } catch (error) {
        return res.status(400).json({
            message: "Error al crear el producto",
            content: error.message,
        });
    }
};

export const listarProductos = async (req, res) => {
    // TODO: agregar el listar productos
    const productos = await Prisma.producto.findMany();
    res.json({
        content: productos,
    });
};

export const devolverProducto = async (req, res) => {
    const { id } = req.params;

    const productoEncontrado = await Prisma.producto.findFirst({
        where: { id: +id },
        include: { categoria: true },
    });

    if (!productoEncontrado) {
        return res.status(400).json({
            message: "El producto no existe",
        });
    }

    return res.json({
        content: productoEncontrado,
    });
};

export const actualizarProducto = async (req,res) => {
    //TODO
    const data = req.body;
    const { id } = req.params;

    //select * from categorias;
    //select id from categorias; 

    const producto = await Prisma.producto.findFirst({
        where: {
            id: +id,
        },
        select: {
            id: true,
        },
    });

    if(!producto) {
        return res.status(400).json({
            message: "El producto no existe",
        });
    }

    const productoActualizado = await Prisma.producto.update({
        where: {
            id: producto.id,
        },
        data: data,
    });

    return res.json({
        message: "Producto actualizado exitosamente",
        content: productoActualizado,
    });
};