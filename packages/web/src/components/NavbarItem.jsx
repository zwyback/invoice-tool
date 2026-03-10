function NavbarItem({ name, href }) {
  return (
    <a
      href={href}
      className="w-full text-gray-400 hover:text-white hover:bg-gray-700 px-4 py-3 text-sm font-medium transition-colors duration-150"
    >
      {name}
    </a>
  );
}

export default NavbarItem;
