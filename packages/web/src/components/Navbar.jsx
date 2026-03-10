import NavbarItem from "./NavbarItem";

function Navbar() {
  return (
    <nav className="fixed left-0 top-0 h-screen w-48 bg-gray-900 border-r border-gray-700 flex flex-col py-6 shadow-lg">
      <h1 className="text-white font-bold text-lg tracking-wide mb-12 px-4">
        Invoice Tool
      </h1>
      <NavbarItem name="Home" href="/" />
      <NavbarItem name="Products" href="/products" />
      <NavbarItem name="Customers" href="/customers" />
      <NavbarItem name="Invoices" href="/invoices" />
    </nav>
  );
}

export default Navbar;
