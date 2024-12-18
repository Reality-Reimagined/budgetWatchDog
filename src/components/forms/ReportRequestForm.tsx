import React from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import type { ReportRequest } from '../../types';

const reportSchema = z.object({
  governmentLevel: z.enum(['federal', 'provincial']),
  province: z.string().optional().nullable(),
  reportType: z.enum(['financial', 'economic', 'demographic']),
  userName: z.string().min(2, 'Name must be at least 2 characters'),
  email: z.string().email('Invalid email address'),
});

interface ReportRequestFormProps {
  onSubmit: (data: ReportRequest) => void;
  isLoading: boolean;
}

export default function ReportRequestForm({ onSubmit, isLoading }: ReportRequestFormProps) {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<ReportRequest>({
    resolver: zodResolver(reportSchema),
  });

  const governmentLevel = watch('governmentLevel');

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
      <div>
        <label className="block text-sm font-medium text-gray-700">
          Government Level
          <select
            {...register('governmentLevel')}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
          >
            <option value="federal">Federal</option>
            <option value="provincial">Provincial</option>
          </select>
        </label>
        {errors.governmentLevel && (
          <p className="mt-1 text-sm text-red-600">{errors.governmentLevel.message}</p>
        )}
      </div>

      {governmentLevel === 'provincial' && (
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Province
            <select
              {...register('province')}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            >
              <option value="">Select a province</option>
              <option value="Alberta">Alberta</option>
              <option value="British Columbia">British Columbia</option>
              <option value="Manitoba">Manitoba</option>
              <option value="New Brunswick">New Brunswick</option>
              <option value="Newfoundland and Labrador">Newfoundland and Labrador</option>
              <option value="Nova Scotia">Nova Scotia</option>
              <option value="Ontario">Ontario</option>
              <option value="Prince Edward Island">Prince Edward Island</option>
              <option value="Quebec">Quebec</option>
              <option value="Saskatchewan">Saskatchewan</option>
            </select>
          </label>
          {errors.province && (
            <p className="mt-1 text-sm text-red-600">{errors.province.message}</p>
          )}
        </div>
      )}

      <div>
        <label className="block text-sm font-medium text-gray-700">
          Report Type
          <select
            {...register('reportType')}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
          >
            <option value="financial">Financial</option>
            <option value="economic">Economic</option>
            <option value="demographic">Demographic</option>
          </select>
        </label>
        {errors.reportType && (
          <p className="mt-1 text-sm text-red-600">{errors.reportType.message}</p>
        )}
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700">
          Your Name
          <input
            type="text"
            {...register('userName')}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
          />
        </label>
        {errors.userName && (
          <p className="mt-1 text-sm text-red-600">{errors.userName.message}</p>
        )}
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700">
          Email Address
          <input
            type="email"
            {...register('email')}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
          />
        </label>
        {errors.email && (
          <p className="mt-1 text-sm text-red-600">{errors.email.message}</p>
        )}
      </div>

      <button
        type="submit"
        disabled={isLoading}
        className="w-full rounded-md bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50"
      >
        {isLoading ? 'Generating Report...' : 'Generate Report'}
      </button>
    </form>
  );
}