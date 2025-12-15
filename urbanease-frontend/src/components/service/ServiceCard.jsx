import { Link } from "react-router-dom"

export default function ServiceCard({ service }) {
  return (
    <div className="bg-white rounded-lg shadow p-4 flex flex-col">
      <div className="h-32 bg-gray-100 rounded mb-3 flex items-center justify-center text-gray-400">
        Image
      </div>

      <h3 className="text-lg font-semibold">{service.name}</h3>
      <p className="text-sm text-gray-500 mt-1 grow">
        {service.description}
      </p>

      <div className="flex justify-between items-center mt-3">
        <span className="font-semibold text-indigo-600">
          ₹{service.base_price}
        </span>
        <span className="text-xs text-gray-400">
          {service.duration_in_minutes} mins
        </span>
      </div>

      <Link
        to={`/services/${service.id}`}
        className="mt-4 bg-indigo-600 text-white text-center py-2 rounded hover:bg-indigo-700"
      >
        Book Now
      </Link>
    </div>
  )
}
